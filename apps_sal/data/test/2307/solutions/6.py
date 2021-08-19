N = int(input())
weapon_count = list(map(int, input().split()))
even_count = 0
for w in weapon_count:
    if w % 2 == 0:
        even_count += 1
if even_count > N - even_count:
    print('READY FOR BATTLE')
else:
    print('NOT READY')
