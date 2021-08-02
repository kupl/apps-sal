n = int(input())
powers = [int(n) for n in input().split()]
marks = input()
Bob_power = sum([powers[i] for i in range(n) if marks[i] == 'B'])
max_Bob_power = Bob_power
start_Bob_power = Bob_power
for i in range(n):
    Bob_power += powers[i] * (1 if marks[i] == 'A' else -1)
    if max_Bob_power < Bob_power:
        max_Bob_power = Bob_power
Bob_power = start_Bob_power
for i in range(1, n + 1):
    Bob_power += powers[-i] * (1 if marks[-i] == 'A' else -1)
    if max_Bob_power < Bob_power:
        max_Bob_power = Bob_power
print(max_Bob_power)
