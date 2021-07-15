s=input()
import string
a=1
for i in s:
    if i in string.ascii_lowercase:
        a*=2
    if i in string.ascii_uppercase:
        a*=3
    if i in string.digits:
        a*=5
print("Too weak" if (a%30 or len(s)<5) else "Correct")

