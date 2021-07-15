X = int(input())
A = int(input())
B = int(input())

# できるだけ買える個数
n = (X - A) // B

print((X - A - B * n))

