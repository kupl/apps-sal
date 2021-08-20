n = input()
print('No') if int(n) % sum(map(int, list(n))) else print('Yes')
