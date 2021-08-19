def countSetBits(num):
    binary = bin(num)
    setBits = [ones for ones in binary[2:] if ones == '1']
    return len(setBits)


t = int(input())
for _ in range(t):
    n = int(input())
    x = countSetBits(n)
    print(2 ** x)
