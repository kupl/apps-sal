n = input()
print('No' if int(n) % sum(map(int, n)) else 'Yes')
