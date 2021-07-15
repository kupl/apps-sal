n = int(input())
s = bin(n)[2:]
print(sum(list(map(int, s))))
