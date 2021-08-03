import numpy as np
import sys
from sys import stdin
import networkx as nx


def main():
    for i in range(t):
        n = a[i][0]
        m = a[i][1]
        G = nx.Graph()
        G.add_nodes_from(range(1, n + 1))
        G.add_edges_from(b[i])
        numn = len(nx.node_connected_component(G, n))
        num1 = len(nx.node_connected_component(G, 1))
        numlv = [num * (num - 1) / 2 + (n - num) * (n - num - 1) / 2 - m for num in range(numn, n - num1 + 1)]
        if(n % 2):
            numl = numlv[0]
        else:
            if((numn - num1) % 2):
                numl = 1
            else:
                numl = numlv[0]
        if(numl % 2):
            print("First")
        else:
            print("Second")
    return


input = sys.stdin.readline
t = int(input())
a = [[0] * 2 for _ in range(t)]
b = [[] for _ in range(t)]
for i in range(t):
    a[i] = list(map(int, input().split()))
    for j in range(a[i][1]):
        b[i].append(tuple(map(int, input().split())))
main()
