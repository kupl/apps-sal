
n, s = list(map(int, input().split()))
a = [i for i in map(int, input().split())]

r = ["NO", "YES"]
z = sum(a) - max(a) <= s
# print(max(a))
print(r[z])
