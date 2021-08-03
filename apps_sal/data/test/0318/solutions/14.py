h, m = map(int, input().split(":"))
m += int(input())
m += h * 60
m %= 24 * 60
print("{:02}:{:02}".format(*divmod(m, 60)))
