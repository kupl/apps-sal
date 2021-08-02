N = int(input())
sum = 10**N
sum -= 9**N
sum -= 9**N
sum += 8**N
print(sum % ((10**9) + 7))
