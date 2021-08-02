n = int(input())
s = input()
x = [s.count(i) for i in ['A', 'C', 'G', 'T']]

z = x.count(max(x))

print((z**n) % (10**9 + 7))
