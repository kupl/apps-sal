import sys
import math


def calcweight_tree(N_vertices, edges, times, inf):
    """
    edges: [start, dest, cost] -> [cost, start, end]
    """
    distance = 0
    passed = [False] * N_vertices
    travel_max = -inf
    for i in range(N_vertices):
        if passed[i] == False:
            distance = 0
            left = i
            cost_sum = 0
            costs = []
            min_distance = inf
            while True:
                dest = edges[left][1]
                cost = edges[dest][0]
                if passed[dest] == False:
                    passed[dest] = True
                    cost_sum += cost
                    costs.append(cost_sum)
                    left = dest
                    if min_distance > cost:
                        min_distance = cost
                else:
                    period = len(costs)
                    increase_period = cost_sum
                    break
            remainder = times % period
            cost_minus = [0]
            for j in range(period - 1):
                cost_minus.append(costs[j])
            if increase_period <= 0:
                '\n                for j in range(period):\n                    costs.append(costs[j]+increase_period)\n                maxindex = 0\n                maxindex_start = 0\n                maxvalue = -inf\n\n                if(remainder==0):\n                    remainder += period\n\n                for st in range(period):\n                    maxvalue_candidate = max(costs[st:st+period])\n                    if(maxvalue_candidate - cost_minus[st] > maxvalue):\n                        maxvalue = maxvalue_candidate - cost_minus[st]\n                        maxindex = costs[st:st+period].index(maxvalue_candidate) + st\n                        maxindex_start = st\n                '
                costs_last = []
                remainder2 = remainder % period
                '\n                for j in range(remainder2, period):\n                    costs_last.append(costs[j])\n                for j in range(0, remainder2):\n                    costs_last.append(costs[j]+increase_period)\n                for j in range(period):\n                    costs_last.append(costs_last[j]+increase_period)\n                '
                for j in range(period):
                    costs_last.append(costs[j])
                for j in range(period):
                    costs_last.append(costs_last[j] + increase_period)
                maxvalue = -inf
                for j in range(period):
                    maxvalue_candidate = max(costs_last[j:j + period])
                    if maxvalue_candidate - cost_minus[j] > maxvalue:
                        maxvalue = maxvalue_candidate - cost_minus[j]
                travel_max = max(maxvalue, travel_max)
            else:
                costs_last = []
                remainder2 = remainder % period
                times_period = times // period - 1
                add_n = times_period * increase_period
                for j in range(remainder2, period):
                    costs_last.append(costs[j] + add_n)
                for j in range(0, remainder2):
                    costs_last.append(costs[j] + add_n + increase_period)
                for j in range(period):
                    costs_last.append(costs_last[j] + increase_period)
                maxvalue = -inf
                for j in range(period):
                    maxvalue_candidate = max(costs_last[j:j + period])
                    if maxvalue_candidate - cost_minus[j] > maxvalue:
                        maxvalue = maxvalue_candidate - cost_minus[j]
                travel_max = max(maxvalue, travel_max)
    return travel_max


def __starting_point():
    """
    N = int( input().strip() )
    Length = list( map(int, input().strip().split() ) )

    edges = [ [] for _ in range(N+2) ]
    for i in range(N):
        edges[0].append([0, i]) #[cost, edge]
    for i in range(1, N+1):
        edges[i].append([0, N+1])
    for i in range(N):
        edges[i].append([ CList[i]*(-1), PList[i] ])
    """
    (N, K) = list(map(int, input().strip().split()))
    PList = list(map(int, input().strip().split()))
    CList = list(map(int, input().strip().split()))
    inf = 10 ** 10
    N_vertices = N
    edges3 = []
    costs = []
    for i in range(N):
        edges3.append([CList[i], PList[i] - 1])
    weight = calcweight_tree(N_vertices, edges3, K, inf)
    print(weight)


__starting_point()
