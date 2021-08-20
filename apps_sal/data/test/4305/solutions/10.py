(hp, attack) = map(int, input().split())
print(hp // attack if hp % attack == 0 else hp // attack + 1)
