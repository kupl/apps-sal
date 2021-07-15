x = int(input())

joy_500 = (x//500) * 1000
joy_5 = ((x % 500)//5) * 5

print(joy_500 + joy_5)
