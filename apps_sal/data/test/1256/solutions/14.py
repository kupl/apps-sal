s = list(map(int, input().split('+')))
s.sort()
print('+'.join(list(map(str, s))))
