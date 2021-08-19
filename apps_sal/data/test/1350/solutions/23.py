n, k = map(int, input().split())
s = input()
d = [0 for _ in range(k)]
for i in s:
    d[ord(i) - ord('A')] += 1
#al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in
print(min(d) * k)
