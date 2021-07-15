n = int(input())
skaitli = list(map(int, input().split()))
isakais = n // 2
skaitli.sort()
isie = skaitli[0:isakais]
garie = skaitli[isakais:]
issum = sum(isie)
garsum = sum(garie)
suma =  issum * issum + garsum * garsum
print(suma)
