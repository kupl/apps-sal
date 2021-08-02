n = input()
enc = input()

i = 0
k = 0
dec = ''

while i < len(enc):
    dec += enc[i]
    k += 1
    i += k

print(dec)
