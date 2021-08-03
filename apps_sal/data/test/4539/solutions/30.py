N = input()
fn = 0
for i in N:
    fn += int(i)

print("Yes" if int(N) % fn == 0 else "No")
