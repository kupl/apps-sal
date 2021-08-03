from sys import stdin

n = int(stdin.readline().strip())
d, x = [int(x) for x in stdin.readline().split()]

a_lst = []
for _ in range(n):
    a_lst.append(int(stdin.readline().strip()))

print(sum([(d - 1) // a + 1 for a in a_lst]) + x)
