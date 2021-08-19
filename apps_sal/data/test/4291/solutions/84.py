(n, q) = list(map(int, input().split()))
s = input()
l = [0 for i in range(len(s))]
for i in range(len(s) - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        l[i + 1] = l[i] + 1
    else:
        l[i + 1] = l[i]
for i in range(q):
    (left, right) = list(map(int, input().split()))
    print(l[right - 1] - l[left - 1])
