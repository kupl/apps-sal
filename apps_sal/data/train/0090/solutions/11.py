t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    st = list(map(int, input().split()))
    sv = []
    for j in range(n):
        if st[j] == 0:
            sv.append(nums[j])
    sv.sort(reverse=True)
    new = []
    k = 0
    for j in range(n):
        if st[j] == 1:
            new.append(nums[j])
        else:
            new.append(sv[k])
            k += 1
    print(*new)
