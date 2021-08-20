S = int(input())
joy_500 = S // 500 * 1000
joy_5 = (S - joy_500 // 2) // 5 * 5
print(joy_500 + joy_5)
