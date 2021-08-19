# A, B, C, D = map(int,input().split())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

fee = [A + C, A + D, B + C, B + D]
fee.sort()
print(fee[0])
