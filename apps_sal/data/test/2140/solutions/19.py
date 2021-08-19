cs = list(input())
m = int(input())
is_ = list(map(int, input().split()))
c_len = len(cs)
is_.append(c_len // 2 + 1)
is_.sort()
for k in range(len(is_) - 1):
    if k % 2 == 1:
        continue
    i = is_[k] - 1
    ni = is_[k + 1] - 1
    for j in range(i, ni):
        (cs[j], cs[c_len - j - 1]) = (cs[c_len - j - 1], cs[j])
print(''.join(cs))
