a = input()
xor_sum = int(a[0])
for i in range(len(a)-1):
    xor_sum = xor_sum ^ int(a[i+1])
if xor_sum == 0:
    print("Exclusive")
else:
    print("Inclusive")
