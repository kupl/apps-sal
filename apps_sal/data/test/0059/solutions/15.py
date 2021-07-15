import sys
n = int(input())

a = list(map(int, input().split()))
s = input()
b = [10**8] * (n+1)

for i in range(len(s)-1, -1, -1):
    b[i] = i if s[i] == '0' else b[i+1]

#print(b)

for i in range(len(a)):
    if a[i] > i + 1:
        if b[i] < a[i]-1:
            print('NO')
            return

print('YES')
