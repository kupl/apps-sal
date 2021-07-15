#include <bits/stdc++.h>
using namespace std;

#define FASTIO ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using ll = long long;

const int MOD = 1e9+7;
const ll INF = 1e18;
const int MAXN = 1e6+5;

int n;
ll s, e[5005], st[5005];

ll f(ll x) {
    int d = 0;
    while(x) {
        int r = x%10;
        x /= 10;
        d += r;
    }
    return (ll) (d*d*d);
}

void precompute() {
    st[0] = s;
    for(int i=1; i<=n; i++) {
        st[i] = st[i-1] + f(st[i-1]);
    }
}

ll dp[5005][5005];
ll xv(int i, int j) {
    if(i == n) return dp[i][j] = st[j]*e[i];
    if(dp[i][j] != -1) return dp[i][j];
    
    dp[i][j] = max(xv(i+1,j+1), st[j]*e[i]+xv(i+1,j));
    return dp[i][j];
}

int main() {
    FASTIO

    memset(dp,-1,sizeof(dp));
    cin >> n >> s;
    for(int i=1; i<=n; i++) cin >> e[i];
    
    precompute();
    cout << xv(1,0) << "\n";
    
    return 0;
}
