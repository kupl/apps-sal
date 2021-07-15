_ = int(input())
as_ = list(sorted(map(int, input().split())))

def get_pair():
    while len(as_) >= 2:
        s0 = as_.pop()
        s1 = as_.pop()
        if s0-1 == s1 or s0 == s1:
            return s1
        as_.append(s1)
    return None

ans = 0
tb = get_pair()
lr = get_pair()
while not (tb is None or lr is None):
    ans += tb * lr
    tb = get_pair()
    lr = get_pair()
print(ans)

