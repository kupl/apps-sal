n = list(map(str, input()))
fn = 0
for i in range(len(n)):
    fn += int(n[i])
print('Yes' if int(''.join(n)) % fn == 0 else 'No')
