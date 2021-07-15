# -*- coding: utf-8 -*-
import numpy as np

iNum = int(input())
naXY = np.zeros((iNum,2))
for iI in range(iNum):
  x, y = list(map(int, input().split()))
  naXY[iI] = [x,y]
naXY0 = np.average(naXY, axis = 0) + np.random.rand(2) * 1e-3
fA = 1.0e-1
while fA > 1.0e-10:
  naP  = naXY - naXY0
  naR = np.einsum("ij, ij -> i", naP,naP)
  iImax = np.argmax(naR)
  #fR  = naR[iImax]**0.5
  naE = naP[iImax]
  #naE/= np.dot(naE,naE)**0.5
  #print(iImax, naXY0, fR)
  #naB = np.einsum("ij, j->i", naP, naE)*2
  #naA = (naR - fR**2 ) / (naB - 1.0e-10 - fR)
  #fA  = np.min(naA[naB< - 1.0e-20])
  #print(iImax, fA, fR)
  #naXY0+=naE*fA
  naXY0+=naE*fA
  fA*=0.9998
print((naR[iImax]**0.5))

