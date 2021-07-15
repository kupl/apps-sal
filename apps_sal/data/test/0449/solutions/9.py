deno = [100,20,10,5,1]
n = int(input())
notes = 0

for i in deno:
    notes += n//i
    n = n - (n//i)*i

print(notes)

