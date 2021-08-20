def pref_counts(string, char):
    result = [0]
    for c in string:
        result.append(result[-1] + (c == char))
    return result


def left_counts(string, char):
    result = [0]
    for c in string:
        result.append(result[-1] + 1 if c == char else 0)
    return result


s = input().replace('C', 'B')
t = input().replace('C', 'B')
(s_bcounts, t_bcounts) = (pref_counts(s, 'B'), pref_counts(t, 'B'))
(s_lcounts, t_lcounts) = (left_counts(s, 'A'), left_counts(t, 'A'))
for i in range(int(input())):
    (a, b, c, d) = list(map(int, input().split()))
    s_b = s_bcounts[b] - s_bcounts[a - 1]
    t_b = t_bcounts[d] - t_bcounts[c - 1]
    s_a = min(s_lcounts[b], b - a + 1)
    t_a = min(t_lcounts[d], d - c + 1)
    answer = False
    if s_b & 1 == t_b & 1:
        if s_b < t_b:
            answer = s_a - (s_b == 0) >= t_a
        elif s_b == t_b:
            answer = s_a >= t_a and (s_a - t_a) % 3 == 0
    print(int(answer), end='')
