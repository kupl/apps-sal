(n, m) = list(map(int, input().split()))
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
oa = len([x for x in A if x % 2])
ob = len([x for x in B if x % 2])
ea = n - oa
eb = m - ob
print(min(oa, eb) + min(ob, ea))
