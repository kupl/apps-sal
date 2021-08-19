N = int(input())
arares = list(map(str, input().split()))
if len([arare for arare in set(arares) if arares.count(arare) > 0]) == 3:
    print('Three')
elif len([arare for arare in set(arares) if arares.count(arare) > 0]) == 4:
    print('Four')
