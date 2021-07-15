n = int(input())
a = input().split()
a = [int(i) for i in a]
odd = []
even = []
s1 = 0
s2 = 0
for i in range(n):
    if i % 2 == 0:
        s1 += a[i]
        odd.append(s1)
        even.append(s2)
    else:
        s2 += a[i]
        odd.append(s1)
        even.append(s2)
ans = 0
for i in range(n):
    if i % 2 == 0:
        if odd[i] - a[i] + even[n - 1] - even[i] == even[i] + odd[n - 1] - odd[i]:
            ans += 1
    else:
        if even[i] - a[i] + odd[n - 1] - odd[i] == odd[i] + even[n - 1] - even[i]:
            ans += 1
print(ans)
