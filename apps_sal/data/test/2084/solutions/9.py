nAndk = input().split()
n, k = [int(i) for i in nAndk]

inp = input().split()
num = [int(i) for i in inp]
num.sort()

ans = num[:k]
print (sum(ans))
