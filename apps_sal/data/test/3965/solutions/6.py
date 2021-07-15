import sys


n = int(input())
L = list(map(int, input().split()))
H = ['a', 'e', 'i', 'o', 'u', 'y']
a = "YES"
for i in range(n):
    ss = input().split()
    s = ""
    ans = 0
    for item in ss:
        for x in item:
            if (x in H):
                ans += 1
    if (ans != L[i]):
        a = "NO"
print(a)

