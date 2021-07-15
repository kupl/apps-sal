# n = input()
# a = input()
# b = input()
# print(n)
# print(a)
# print(b)
# import sys
# sys.setrecursionlimit(1000000)
# try:
n = int(input())
burles = list(map(int, input().split()))
directions = list(map(int, input().split()))

burles.insert(0,0)
directions.insert(0,0)


v = [0]*(n+1)# visitou
g = [0]*(n+1)# grupo



def passa(pos):

	nonlocal current_group
	nonlocal v
	nonlocal g
	nonlocal soma_total
	pilha = [-1]
	avanco = True
	# print('posicao {} {}'.format(pos, v[pos]))
	# print('Visita {}'.format(pos))
	grupo = 0
	esta_no_ciclo = False
	menor_local = 0
	while pilha:
		
		if avanco:

			if v[pos] == 1:
				v[pos] = 2
				if g[pos] == 0:
					g[pos] = current_group
					# print('atribui grupo {}'.format(current_group))
					current_group+=1
				
				grupo = g[pos]
				avanco = False
				esta_no_ciclo = True
				menor_local = burles[pos]

			elif v[pos] == 2 or v[pos] == 3:
				grupo = g[pos]
				avanco = False
				esta_no_ciclo = False
				grupo = g[pos]
			else:	
				v[pos] = 1
				pilha.append(pos)
				pos = directions[pos]
		
		# g[pos], ver, minimo = passa(directions[pos])
		
		else:
			pos = pilha.pop(len(pilha)-1)
			if pos < 0:
				continue
			g[pos] = grupo
			if v[pos] ==2 and esta_no_ciclo:
				soma_total+=menor_local
				esta_no_ciclo = False

				# return g[pos], False, 0

			elif v[pos] ==1 and esta_no_ciclo:
				v[pos] = 2
				menor_local = min(menor_local, burles[pos])
				# return g[pos], True, min(minimo, burles[pos])
			
			if v[pos] ==1 and not esta_no_ciclo:
				v[pos] = 3

				# return g[pos], False, 0


			# return g[pos], False, 0
	# print('atribui grupo {}'.format(g[pos]))

current_group = 1
soma_total = 0
for i in range(1, n+1):
	if v[i] ==0:
		passa(i)
print(soma_total)
# except Exception:
# print(sys.exc_info()[2])



# dicionario = {}
# for i in range(1, n+1):
# 	if v[i] == 2:
# 		grupo = g[i]
# 		menor = dicionario.get(grupo, None)
# 		if menor:
# 			dicionario[grupo] = min(menor, burles[i])

# 		else:
# 			dicionario[grupo] = burles[i]

# print(int(sum(dicionario.values())))

# except RuntimeError as e:
# 	print(1)
# 	print(str(e))

# print(g)
# print(v)

# conjunto = set()
# soma = 0
# for i in range(1, len(p)):
# 	if g[i] not in conjunto:
# 		conjunto.add(g[i])
# 		soma+=p[i]



# answer = 0

# for i in range(1,n+1):
#     node = i
#     while g[node] == 0:
#         g[node] = i
#         node = a[node]
#     if g[node] != i:
#         continue
#     current = node
#     min_cost = c[node]
#     while a[node] != current:
#         node = a[node]
#         min_cost = min(min_cost,c[node])
#     answer += min_cost

# print(answer)
# print(v)
# print(g)
# print(p)
# print(dicionario)

