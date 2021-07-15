str = input()
small = 0
big = 0
num = 0
for i in range(10):
    if chr(i + ord('0')) in str:
        num = 1
for i in range(26):
    if chr(i + ord('a')) in str:
        small = 1
for i in range(26):
    if chr(i + ord('A')) in str:
        big = 1
if len(str) >= 5 and big and small and num:
    print("Correct")
else:
    print("Too weak")

