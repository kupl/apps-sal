no_islands = int(input())
initial = input().split()
final = input().split()
initial.remove('0')
final.remove('0')

first = initial.index(final[0])
if initial[first:] + initial[:first] == final:
    print('YES')
else:
    print('NO')
