numero = input()
soma = 0

for n in numero:
    soma += int(n)

print(f"{'Yes' if  soma%9 == 0 else 'No'}")
