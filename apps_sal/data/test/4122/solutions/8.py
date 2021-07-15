from math import floor

(H, n) = (int(x) for x in input().split())
d = [int(x) for x in input().split()]

sum_d = sum(d)

max_damage_per_round = 0
damage_sofar = 0
for attack in d:
	damage_sofar += attack
	max_damage_per_round = min(max_damage_per_round, damage_sofar)

max_damage_per_round = abs(max_damage_per_round)

answer = 0

for attack in d:
	answer += 1
	H += attack
	if H <= 0:
		print(answer)
		return

if sum_d >= 0:
	print(-1)
	return

if H > max_damage_per_round:
	can_attack_rounds_count = floor((H - max_damage_per_round - 1) / abs(sum_d))
	answer += n * can_attack_rounds_count
	H += sum_d * can_attack_rounds_count

if H <= 0:
	print(answer)
	return

while True:
	for attack in d:
		answer += 1
		H += attack
		if H <= 0:
			print(answer)
			return
