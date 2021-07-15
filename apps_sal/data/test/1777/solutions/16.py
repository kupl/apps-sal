import collections

def pos_score(S):
    s = 0
    for c in S:
        if c == '(':
            s += 1
        elif c == ')':
            s -= 1
        if s < 0:
            return None
    return s

def neg_score(S):
    s = 0
    for c in reversed(S):
        if c == '(':
            s += 1
        elif c == ')':
            s -= 1
        if s > 0:
            return None
    return s

def score(S):
    p = pos_score(S)
    if p is not None:
        return p
    n = neg_score(S)
    if n is not None:
        return n
    return None

N = int(input())
scores = [score(input()) for _ in range(N)]
score_neg_map = collections.Counter(-sc for sc in scores if sc is not None and sc < 0)
score_pos_map = collections.Counter(sc for sc in scores if sc is not None and sc > 0)
score_zero = sum(sc == 0 for sc in scores)

ans = score_zero // 2
for key in score_pos_map:
    pos = score_pos_map[key]
    neg = score_neg_map.get(key, 0)
    ans += min(pos, neg)
print(ans)

