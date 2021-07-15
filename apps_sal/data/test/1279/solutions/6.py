n,m = list(map(int,input().split()))
chests = list(map(int,input().split()))
keys = list(map(int,input().split()))

even_chests = sum((x+1)%2 for x in chests)
odd_chests = sum((x)%2 for x in chests)
even_keys = sum((x+1)%2 for x in keys)
odd_keys = sum((x)%2 for x in keys)
print(min(even_chests,odd_keys)+min(odd_chests,even_keys))

