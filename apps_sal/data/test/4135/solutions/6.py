n = int(input())
string = input()
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
for d in divisors:
    string = string[:d][::-1] + string[d:]
print(string)
