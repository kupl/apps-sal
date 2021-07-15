n, k = list(map(int, input().split()))
s = list(input())

tmp = s.pop(k - 1)
l = tmp.lower()
s.insert(k - 1, l)
print((''.join(s)))

