n = int(input())
s = input().split()

print('Three') if len(set(s)) == 3 else print('Four')
