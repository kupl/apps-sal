def f(x):
    if (x.count("8")):
        return True
    return False


a = int(input());

c = 1;
a += 1;

a = str(a)

while not f(a):
    a = str(int(a) + 1);
    c += 1;

print(c)
