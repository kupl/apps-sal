a, b = map(int, input().split(' '))

mod_ab = (a * b) % 2

if(mod_ab == 0):
    print("Even")
else:
    print("Odd")
