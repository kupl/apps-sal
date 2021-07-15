n = input()

n = n.replace("9", "@")
n = n.replace("1", "9")
n = n.replace("@", "1")


print((int(n)))

