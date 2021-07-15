field = "A" + input() + "A"
letters = ["A", "E", "I", "O", "U", "Y"]
ans = 1
last_let = 0
for i in range(len(field)):
    let = field[i]
    if let in letters:
        ans = max(ans, i - last_let)
        last_let = i
print(ans)
